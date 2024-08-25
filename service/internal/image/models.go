package image

import (
	"time"

	"github.com/google/uuid"
)

type Image struct {
	ID           uuid.UUID
	CreatedAt    time.Time
	OriginalLink string
}
