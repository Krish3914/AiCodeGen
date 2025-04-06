import { TestBed } from '@angular/core/testing';

import { LeavemanagementserviceService } from './leavemanagementservice.service';

describe('LeavemanagementserviceService', () => {
  let service: LeavemanagementserviceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LeavemanagementserviceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
