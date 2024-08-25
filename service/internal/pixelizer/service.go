package pixelizer

import (
	"time"

	"github.com/nifle3/pixelizer/service/internal/image"
	"github.com/segmentio/kafka-go"
)

var _ image.Pixelizer = &Pixelizer{}

type Pixelizer struct {
	writer kafka.Writer
}

func New(brokers []string, topicName string, batchSize int, batchTimeout, writeTimeout, readTimeout time.Duration) *Pixelizer {
	writer := &kafka.Writer{
		Addr: kafka.TCP(brokers...),
		Topic: topicName,
		Balancer: &kafka.LeastBytes{},
		BatchSize: batchSize,
		BatchTimeout: batchTimeout,
		WriteTimeout: writeTimeout,
		ReadTimeout: readTimeout,
		Async: false,
		RequiredAcks: kafka.RequireAll,
	}

	return Pixelizer{
		writer: writer,
	}
}

func (p *Pixelizer) Pixelize(input image.Image) error {
	p.writer.WriteMessages(context.)
}
