import { TestBed } from '@angular/core/testing';

import { InvokeContentGeneratorService } from './invoke-content-generator.service';

describe('InvokeContentGeneratorService', () => {
  let service: InvokeContentGeneratorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InvokeContentGeneratorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
