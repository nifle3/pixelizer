package image

import (
	"context"
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

func (s *Service) Pixelize(ctx context.Context, imageFile io.Reader) (uuid.UUID, error) {
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
		OriginalLink: fileLink.String(),
	}

	if err := s.repo.Add(ctx, image, imageFile); err != nil {
		return uuid.UUID{}, err
	}

	if err := s.pixelizer.Pixelize(ctx, image); err != nil {
		return uuid.UUID{}, err
	}

	if err := s.repo.MarkAsSend(ctx, image.ID); err != nil {
		return uuid.UUID{}, err
	}

	return id, nil
}

func (s *Service) Get(ctx context.Context, id uuid.UUID) (Image, error) {
	return s.repo.Get(ctx, id)
}

func (s *Service) GetAll(ctx context.Context) ([]Image, error) {
	return s.repo.GetAll(ctx)
}

func (s *Service) GetAllForUser(ctx context.Context,, userID uuid.UUID) ([]Image, error) {
	return s.repo.GetAllForUserId(ctx, userID)
}

func (s *Service) Delete() error {
	panic("Not implemeted yet")
}

func (s *Service) SendAllNotSent(ctx context.Context,) error {
	var generalErr error

	images, generalErr := s.repo.GetAllNotSend(ctx)
	if generalErr != nil {
		return generalErr
	}

	for _, value := range images {
		if err := s.pixelizer.Pixelize(ctx, value); err != nil {
			generalErr = errors.Join(generalErr, err)
		}
	}

	return generalErr
}
