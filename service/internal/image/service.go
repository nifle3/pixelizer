package image

import (
	"io"
	"time"

	"github.com/google/uuid"
)

type Service struct {
	repo      Repository
	pixelizer Pixelizer
}

func New() *Service {
	return &Service{}
}

func (s *Service) Pixelize(imageFile io.Reader) error {
	id, err := uuid.NewRandom()
	if err != nil {
		return err
	}

	fileLink, err := uuid.NewV6()
	if err != nil {
		return err
	}

	image := Image{
		ID:           id,
		CreatedAt:    time.Now(),
		OriginalLink: fileLink,
	}

	if err := s.repo.add(image, imageFile); err != nil {
		return err
	}

	if err := s.pixelizer.pixelize(image); err != nil {
		return err
	}

	if err := s.repo.markAsCheck(image.ID); err != nil {
		return err
	}

	return nil
}

func (s *Service) Get() error {
	return nil
}

func (s *Service) GetAll() error {
	return nil
}

func (s *Service) GetAllUser() error {
	return nil
}

func (s *Service) Delete() error {
	return nil
}
