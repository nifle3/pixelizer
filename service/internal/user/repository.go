package user

import "github.com/google/uuid"

type Repository interface {
	add() error
	update() error
	updatePassword(userID uuid.UUID, password string) error
	delete() error
	get(id uuid.UUID) (User, error)
}
