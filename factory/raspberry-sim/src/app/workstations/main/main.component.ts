import { Component, OnInit } from '@angular/core';
import {WorkstationService} from '../../core/service/workstation.service';
import {interval, Observable} from 'rxjs';
import {switchMap, tap} from 'rxjs/operators';
import {ILight} from '../../core/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  poller: Observable<{ [key: string]: ILight }>;
  light1Label: string;
  light1Color: string;
  light2Label: string;
  light2Color: string;
  light3Label: string;
  light3Color: string;
  light4Label: string;
  light4Color: string;
  light5Label: string;
  light5Color: string;
  light6Label: string;
  light6Color: string;
  worker3Label: string;
  worker3Color: string;

  constructor(private workstationService: WorkstationService) { }

  ngOnInit() {
    this.poller = interval(500)
    .pipe(
      switchMap(() => this.workstationService.get('main')),
      tap(lights => {
        Object.keys(lights).forEach(key => {
          this[key + 'Color'] = lights[key]['color'] === 'off' ? '' : lights[key]['color'];
          this[key + 'Label'] = lights[key]['label'];
        });
      })
    );
  }

}
