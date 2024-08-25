package image

import (
	"io"

	"github.com/google/uuid"
)

type Repository interface {
	Add(image Image, file io.Reader) error
	GetAll() ([]Image, error)
	GetAllForUserId(userID uuid.UUID) ([]Image, error)
	Get(id uuid.UUID) (Image, error)
	Delete(id uuid.UUID) error
	MarkAsSend(id uuid.UUID) error
	GetAllNotSend() ([]Image, error)
}
