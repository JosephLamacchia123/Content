import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Profile } from './dropdown/dropdown.component';

@Injectable({
  providedIn: 'root'
})
export class ProfileManagerService {

  private selectedProfile: Profile|null = null;

  setSelectedProfile(option: Profile | null) {
    this.selectedProfile = option;
  }

  getSelectedProfile() : Profile | null{
    return this.selectedProfile;
  }

  constructor() { }
}
