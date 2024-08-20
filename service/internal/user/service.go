package user

import (
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

func (s *Service) Add(user User) error {
	passwordBytes := []byte(user.Password)
	hashedPassword, err := bcrypt.GenerateFromPassword(passwordBytes, bcrypt.DefaultCost)
	if err != nil {
		return err
	}

	user.Password = string(hashedPassword)

	return s.repo.add()
}

func (s *Service) Update(user User) error {
	return s.repo.update()
}

func (s *Service) UpdatePassword(userID uuid.UUID, newPassword string, pastPassword string) error {
	user, err := s.repo.get(userID)
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

	return s.repo.updatePassword(userID, stringHashPassword)
}

func (s *Service) Delete(user User) error {
	return s.repo.delete()
}
