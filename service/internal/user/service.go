package user

import (
	"context"

	"github.com/google/uuid"
	"golang.org/x/crypto/bcrypt"
)

type Service struct {
	repo Repository
}

func New() *Service {
	return &Service{
		repo: nil,
	}
}

func (s *Service) Add(ctx context.Context, user User) error {
	var err error
	user.Id, err = uuid.NewV6()
	if err != nil {
		return err
	}

	passwordBytes := []byte(user.Password)
	hashedPassword, err := bcrypt.GenerateFromPassword(passwordBytes, bcrypt.DefaultCost)
	if err != nil {
		return err
	}

	user.Password = string(hashedPassword)

	return s.repo.add(ctx, user)
}

func (s *Service) Update(ctx context.Context, user User) error {
	return s.repo.update(ctx, user)
}

func (s *Service) UpdatePassword(ctx context.Context, userID uuid.UUID, newPassword string, pastPassword string) error {
	user, err := s.repo.get(ctx, userID)
	if err != nil {
		return err
	}

	if err := bcrypt.CompareHashAndPassword([]byte(user.Password), []byte(pastPassword)); err != nil {
		return err
	}

	passwordBytes := []byte(newPassword)
	hashedPassword, err := bcrypt.GenerateFromPassword(passwordBytes, bcrypt.DefaultCost)
	if err != nil {
		return err
	}

	stringHashPassword := string(hashedPassword)

	return s.repo.updatePassword(ctx, userID, stringHashPassword)
}

func (s *Service) Delete(ctx context.Context, user User) error {
	return s.repo.delete(ctx, user.Id)
}
