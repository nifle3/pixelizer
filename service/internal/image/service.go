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

func (s *Service) Pixelize(imageFile io.Reader) (uuid.NullUUID, error) {
	id, err := uuid.NewRandom()
	if err != nil {
		return uuid.NullUUID{Valid: false}, err
	}

	fileLink, err := uuid.NewV6()
	if err != nil {
		return uuid.NullUUID{Valid: false}, err
	}

	image := Image{
		ID:           id,
		CreatedAt:    time.Now(),
		OriginalLink: fileLink,
	}

	if err := s.repo.add(image, imageFile); err != nil {
		return uuid.NullUUID{Valid: false}, err
	}

	if err := s.pixelizer.pixelize(image); err != nil {
		return uuid.NullUUID{Valid: false}, err
	}

	if err := s.repo.markAsSend(image.ID); err != nil {
		return uuid.NullUUID{Valid: false}, err
	}

	return uuid.NullUUID{UUID: id, Valid: true}, nil
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

func (s *Service) SendAllNotSent() error {
	var generalErr error

	images, generalErr := s.repo.getAllNotSend()
	if generalErr != nil {
		return generalErr
	}

	for _, value := range images {
		if err := s.pixelizer.pixelize(value); err != nil {
			generalErr = errors.Join(generalErr, err)
		}
	}

	return generalErr
}
