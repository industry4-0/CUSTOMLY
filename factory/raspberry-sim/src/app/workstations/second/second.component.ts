import { Component, OnInit } from '@angular/core';
import {WorkstationService} from '../../core/service/workstation.service';
import {interval, Observable} from 'rxjs';
import {switchMap, tap} from 'rxjs/operators';
import {ILight} from '../../core/models';

@Component({
  selector: 'app-second',
  templateUrl: './second.component.html',
  styleUrls: ['./second.component.scss']
})
export class SecondComponent implements OnInit {

  poller: Observable<{ [key: string]: ILight }>;
  light1Label: string;
  light2Label: string;
  light1Color: string;
  light2Color: string;
  worker2Label: string;
  worker2Color: string;

  constructor(private workstationService: WorkstationService) { }

  ngOnInit() {
    this.poller = interval(500)
    .pipe(
      switchMap(() => this.workstationService.get('sub', 2)),
      tap(lights => {
        Object.keys(lights).forEach(key => {
          this[key + 'Color'] = lights[key]['color'] === 'off' ? '' : lights[key]['color'];
          this[key + 'Label'] = lights[key]['label'];
        });
      })
    );
  }

}
