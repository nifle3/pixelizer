package app

import (
	"fmt"
	"log/slog"
	"os"

	"github.com/nifle3/pixelizer/service/internal/config"
	"github.com/nifle3/pixelizer/service/internal/transport/frontend"
)

func Run() {
	cfg, err := config.New("./config.yaml")
	if err != nil {
		slog.Error(fmt.Sprintf("Error from config: %s \n", err.Error()))
		os.Exit(1)
	}

	if err := frontend.Start(cfg.Server.Port); err != nil {
		slog.Error(fmt.Sprintf("Error from fiber %s \n", err.Error()))
		os.Exit(1)
	}
}
