import { Component, Input,DoCheck  } from '@angular/core';
import { ProfileManagerService } from '../profilemanager.service';
import { Profile } from '../dropdown/dropdown.component';

@Component({
  selector: 'profileimage',
  templateUrl: './profileimage.component.html',
  styleUrls: ['./profileimage.component.css']
})



export class ProfileimageComponent {

  constructor(profileService: ProfileManagerService){
    this.profileService = profileService;
  }

  @Input() imageUrl: string = "";
  @Input() imageAlt: string =  "";
  activeProfile:Profile|null = null;

  profileService:ProfileManagerService;


  ngDoCheck(){
    this.activeProfile = this.profileService.getSelectedProfile();
    console.log("Ative Profile :: ")
    if(this.activeProfile){
        this.imageUrl = this.activeProfile.fields['imageUrl'];
        console.log(this.imageUrl)
    }
  }
}
