package image

type Pixelizer interface {
	pixelize(image Image) error
}
