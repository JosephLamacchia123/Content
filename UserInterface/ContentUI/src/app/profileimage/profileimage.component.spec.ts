import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfileimageComponent } from './profileimage.component';

describe('ProfileimageComponent', () => {
  let component: ProfileimageComponent;
  let fixture: ComponentFixture<ProfileimageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProfileimageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProfileimageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

});
