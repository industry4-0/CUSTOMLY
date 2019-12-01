import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-arm',
  templateUrl: './arm.component.html',
  styleUrls: ['./arm.component.scss']
})
export class ArmComponent implements OnInit {
  @Input() color: string;
  @Input() label: string;

  constructor() { }

  ngOnInit() {
  }

}
