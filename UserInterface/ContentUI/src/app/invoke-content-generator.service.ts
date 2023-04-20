import { Injectable } from '@angular/core';
import  from 'aws-sdk';


@Injectable({
  providedIn: 'root'
})
export class InvokeContentGeneratorService {
  private stepFunctions: AWS.StepFunctions;

  private apiGateWayUrl:string = "";
  constructor() {
    this.stepFunctions = new AWS.StepFunctions();
   }

   public async invokeStepFunction(input: object): Promise<AWS.StepFunctions.StartExecutionOutput> {
    const params: AWS.StepFunctions.StartExecutionInput = {
      stateMachineArn: 'your_step_function_arn',
      input: JSON.stringify(input),
    };

    return new Promise((resolve, reject) => {
      this.stepFunctions.startExecution(params, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    });
  }
}
