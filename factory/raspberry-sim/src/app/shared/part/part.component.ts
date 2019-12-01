import {Component, Input, OnInit} from '@angular/core';
import {animate, state, style, transition, trigger} from '@angular/animations';

@Component({
  selector: 'app-part',
  templateUrl: './part.component.html',
  styleUrls: ['./part.component.scss']
})
export class PartComponent implements OnInit {
  @Input() label: string = 'Part';
  @Input() color: string = '';

  working: boolean = false;

  constructor() { }

  ngOnInit() {

  }

}
