package kafkawriter

import (
	"time"

	"github.com/segmentio/kafka-go"
)

func New(brokers []string, topicName string, batchSize int, batchTimeout, writeTimeout, readTimeout time.Duration) *kafka.Writer {
	return &kafka.Writer{
		Addr:         kafka.TCP(brokers...),
		Topic:        topicName,
		Balancer:     &kafka.LeastBytes{},
		BatchSize:    batchSize,
		BatchTimeout: batchTimeout,
		WriteTimeout: writeTimeout,
		ReadTimeout:  readTimeout,
		Async:        false,
		RequiredAcks: kafka.RequireAll,
	}
}
