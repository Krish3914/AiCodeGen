import { TestBed } from '@angular/core/testing';

import { PodserviceService } from './podservice.service';

describe('PodserviceService', () => {
  let service: PodserviceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PodserviceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
