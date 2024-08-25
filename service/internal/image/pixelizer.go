package image

type Pixelizer interface {
	Pixelize(image Image) error
}
