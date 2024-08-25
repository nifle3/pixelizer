package image

import "context"

type Pixelizer interface {
	Pixelize(ctx context.Context, image Image) error
}
