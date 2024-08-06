package config

import (
	"time"

	"github.com/ilyakaznacheev/cleanenv"
)

type ServerConfig struct {
	Port        string        `yaml:"port" env:"SERVER_PORT"`
	IdleTimeout time.Duration `yaml:"idle_timeout" env:"SERVER_IDLE_TIMEOUT"`
}

type Config struct {
	Server ServerConfig `yaml:"server"`
}

func New(path string) (Config, error) {
	config := Config{}
	err := cleanenv.ReadConfig(path, &config)
	return config, err
}
