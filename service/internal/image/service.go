package image

import (
	"errors"
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

func (s *Service) Pixelize(imageFile io.Reader) (uuid.UUID, error) {
	id, err := uuid.NewRandom()
	if err != nil {
		return uuid.UUID{}, err
	}

	fileLink, err := uuid.NewV6()
	if err != nil {
		return uuid.UUID{}, err
	}

	image := Image{
		ID:           id,
		CreatedAt:    time.Now(),
		OriginalLink: fileLink,
	}

	if err := s.repo.Add(image, imageFile); err != nil {
		return uuid.UUID{}, err
	}

	if err := s.pixelizer.Pixelize(image); err != nil {
		return uuid.UUID{}, err
	}

	if err := s.repo.MarkAsSend(image.ID); err != nil {
		return uuid.UUID{}, err
	}

	return id, nil
}

func (s *Service) Get(id uuid.UUID) (Image, error) {
	return s.repo.Get(id)
}

func (s *Service) GetAll() ([]Image, error) {
	return s.repo.GetAll()
}

func (s *Service) GetAllForUser(userID uuid.UUID) ([]Image, error) {
	return s.repo.GetAllForUserId(userID)
}

func (s *Service) Delete() error {
	panic("Not implemeted yet")
}

func (s *Service) SendAllNotSent() error {
	var generalErr error

	images, generalErr := s.repo.GetAllNotSend()
	if generalErr != nil {
		return generalErr
	}

	for _, value := range images {
		if err := s.pixelizer.Pixelize(value); err != nil {
			generalErr = errors.Join(generalErr, err)
		}
	}

	return generalErr
}
