package image

import (
	"context"
	"io"

	"github.com/google/uuid"
)

type Repository interface {
	Add(ctx context.Context, image Image, file io.Reader) error
	GetAll(ctx context.Context) ([]Image, error)
	GetAllForUserId(ctx context.Context, userID uuid.UUID) ([]Image, error)
	Get(ctx context.Context, id uuid.UUID) (Image, error)
	Delete(ctx context.Context, id uuid.UUID) error
	MarkAsSend(ctx context.Context, id uuid.UUID) error
	GetAllNotSend(ctx context.Context) ([]Image, error)
}
