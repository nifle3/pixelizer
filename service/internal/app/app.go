package app

import (
	"context"
	"fmt"
	"log/slog"
	"os"
	"os/signal"
	"syscall"

	"github.com/nifle3/pixelizer/service/internal/config"
	"github.com/nifle3/pixelizer/service/internal/transport/frontend"
)

func Run() {
	ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
	defer cancel()

	cfg, err := config.New("./config.yaml")
	if err != nil {
		slog.Error(fmt.Sprintf("Error from config: %s \n", err.Error()))
		os.Exit(1)
	}

	server := frontend.New(ctx, cfg.Server)
	go func() {
		if err := server.Start(); err != nil {
			slog.Error(fmt.Sprintf("Error from listening server %s \n", err.Error()))
			os.Exit(1)
		}
	}()

	server.GracefulShutdown()
}
