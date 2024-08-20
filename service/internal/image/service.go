package image

type Service struct {
}

func New() *Service {
	return &Service{}
}

func (s *Service) Pixelize() error {
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
