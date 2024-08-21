package image

import (
	"io"

	"github.com/google/uuid"
)

type Repository interface {
	add(image Image, file io.Reader) error
	delete(id uuid.UUID) error
	markAsSend(id uuid.UUID) error
	getAllNotSend() ([]Image, error)
}
