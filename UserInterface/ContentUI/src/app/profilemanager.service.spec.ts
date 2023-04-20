import { TestBed } from '@angular/core/testing';

import { ProfileManagerService } from './profilemanager.service';

describe('ProfilemanagerService', () => {
  let service: ProfileManagerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProfileManagerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
