import { Component } from '@angular/core';
import { ProfileManagerService } from '../profilemanager.service';
import { Profile } from '../dropdown/dropdown.component';


@Component({
  selector: 'generate-content',
  templateUrl: './generate-content.component.html',
  styleUrls: ['./generate-content.component.css']
})
export class GenerateContentComponent {
  activeProfile:Profile|null = null;
  constructor(private profileService:ProfileManagerService, private contentGeneratorService:InvokeContentGeneratorService) {}

  generateContent() {
  
  }

  ngDoCheck(){
    this.activeProfile = this.profileService.getSelectedProfile(); 
  }

  async invokeStepFunction() {
    const input = {
      key1: 'value1',
      key2: 'value2',
    };

    try {
      const result = await this.contentGeneratorService.invokeStepFunction(input);
      console.log('Step Function execution started:', result);
    } catch (error) {
      console.error('Error starting Step Function execution:', error);
    }
  }
}

