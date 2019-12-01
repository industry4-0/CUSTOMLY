import {Component, OnInit, ViewChild} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {MatCheckboxChange, MatStepper} from '@angular/material';
import {IType} from '../core/models/part.model';
import {newOrder, viewOrder, viewClientOrders, testDeployment} from '../blockchain/eshop';
import {ApiService} from '../core/service/api.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.scss']
})
export class OrderComponent implements OnInit {
  @ViewChild('stepper', {static: false}) private myStepper: MatStepper;

  cellphone: FormGroup;
  dualMicChecked: boolean = false;
  isDualMic: boolean = false;

  constructor(private formBuilder: FormBuilder, private apiService: ApiService) {
  }

  ngOnInit(): void {
    this.cellphone = this.formBuilder.group({
      camera: [null],
      battery: [null],
      speaker: [null],
      display: [null],
      microphone: [null],
      processor: [null],
    });
  }

  onNextClick(index: number): void {
    console.log(index);
    this.myStepper.next();
  }

  onMicCheckboxChange(event: MatCheckboxChange) {

    this.isDualMic = event.checked;
  }

  onSubmit(): void {
    this.manipulateForm();
    console.log(this.cellphone.value);
    this.apiService.post('orders', this.cellphone.value).subscribe();
    try {
      newOrder(2, JSON.stringify(this.cellphone.value))
      .then(function(res) {
        console.log(`Blockchain result: ${res}`);
      })
      .catch(function(err) {
        console.error(err);
      });
    } catch(e) {
      console.log('Chain hiccup');
    }
  }

  private manipulateForm(): void {
    const screenSize = this.cellphone.get('display').value;
    const cpuName = this.cellphone.get('processor').value;
    const batteryCapacity = this.cellphone.get('battery').value;
    const speakerType = this.cellphone.get('speaker').value;
    const cameraPixel = this.cellphone.get('camera').value;

    this.cellphone.get('display').setValue({size: screenSize});
    this.cellphone.get('processor').setValue({model: cpuName});
    this.cellphone.get('battery').setValue({capacity: batteryCapacity});
    this.cellphone.get('speaker').setValue((speakerType === 'stereo') ? {stereo: true} : {frontfacing: true});
    this.cellphone.get('microphone').setValue({dual: this.isDualMic});
    this.cellphone.get('camera').setValue({megapixel: cameraPixel});

  }

}
