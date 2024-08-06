package frontend

import (
	"github.com/gofiber/fiber/v2"
)

func Start(port string) error {
	app := fiber.New()

	app.Static("/", "./static")

	return app.Listen(":" + port)
}
