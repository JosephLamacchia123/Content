import { Component } from '@angular/core';
import { ProfileManagerService } from '../profilemanager.service';

export interface Profile {
  value: string;
  fields: { [key: string]: string };
}


@Component({
  selector: 'profile-dropdown',
  templateUrl: './dropdown.component.html',
  styleUrls: ['./dropdown.component.css']
})
export class DropdownComponent {
  selectedProfile: Profile | null = null;

  options: Profile[] = [
    {
      value: 'Bill Banes',
      fields: {
        imageUrl: 'assets/BillBanes.png',
        description: 'Motivational speaker who posts uplifting content.',
      },
    },
    {
      value: 'Tom Yort',
      fields: {
        imageUrl: 'assets/TomYort.png',
        description: 'News reporter who posts summaries of recent news articles.',
      },
    }
  ];

  onItemSelected(option: Profile) {
    this.selectedProfile = option;
    console.log(this.selectedProfile);
    this.profileManager.setSelectedProfile(this.selectedProfile);
  }

  constructor(private profileManager:ProfileManagerService){

  }



}
