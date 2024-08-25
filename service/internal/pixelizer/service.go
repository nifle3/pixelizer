package pixelizer

import (
	"context"

	"github.com/nifle3/pixelizer/service/internal/image"
	"github.com/segmentio/kafka-go"
)

var _ image.Pixelizer = &Pixelizer{}

type Pixelizer struct {
	writer *kafka.Writer
}

func New(writer *kafka.Writer) *Pixelizer {
	return &Pixelizer{
		writer: writer,
	}
}

func (p *Pixelizer) Pixelize(ctx context.Context, input image.Image) error {
	key, err := input.ID.MarshalBinary()
	if err != nil {
		return err
	}

	err = p.writer.WriteMessages(ctx, kafka.Message{
		Key:   key,
		Value: []byte(input.OriginalLink),
	})

	return err
}
