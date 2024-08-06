package frontend

import (
	"context"
	"log/slog"
	"time"

	"github.com/nifle3/pixelizer/service/internal/config"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
)

type Server struct {
	ctx  context.Context
	app  *fiber.App
	port string
}

func New(ctx context.Context, cfg config.ServerConfig) Server {
	engine := html.New("./template", ".html")

	app := fiber.New(fiber.Config{
		Views:       engine,
		ReadTimeout: time.Second * 2,
		IdleTimeout: cfg.IdleTimeout,
	})

	app.Static("/", "./static")

	app.Get("/ping", func(c *fiber.Ctx) error {
		slog.Info("ping waiting")
		time.Sleep(time.Second * 5)
		slog.Info("ping waited end")
		return nil
	})

	return Server{
		app:  app,
		ctx:  ctx,
		port: cfg.Port,
	}
}

func (s *Server) Start() error {
	return s.app.Listen(":" + s.port)
}

func (s *Server) GracefulShutdown() error {
	<-s.ctx.Done()
	slog.Info("Graceful shutdown started")

	s.app.Server().DisableKeepalive = true

	for s.app.Server().GetOpenConnectionsCount() > 0 {
		time.Sleep(time.Second)
	}

	if err := s.app.Shutdown(); err != nil {
		return err
	}

	slog.Info("Graceful shutdown succesful")
	return nil
}
