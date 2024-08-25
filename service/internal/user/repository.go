package user

import (
	"context"

	"github.com/google/uuid"
)

type Repository interface {
	add(ctx context.Context, user User) error
	update(ctx context.Context, user User) error
	updatePassword(ctx context.Context, userID uuid.UUID, password string) error
	delete(ctx context.Context, id uuid.UUID) error
	get(ctx context.Context, id uuid.UUID) (User, error)
}
