package user

import (
	"time"

	"github.com/google/uuid"
)

type User struct {
	Id        uuid.UUID
	Nickname  string
	Password  string
	Email     string
	LastEnter time.Duration
	LastIP    string
}
