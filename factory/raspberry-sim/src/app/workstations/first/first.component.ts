import {Component, OnInit} from '@angular/core';
import {from, interval, Observable, of} from 'rxjs';
import {delay, map, mergeMap, switchMap, tap} from 'rxjs/operators';
import {WorkstationService} from '../../core/service/workstation.service';
import {ILight} from '../../core/models';

@Component({
  selector: 'app-first',
  templateUrl: './first.component.html',
  styleUrls: ['./first.component.scss']
})
export class FirstComponent implements OnInit {

  poller: Observable<{ [key: string]: ILight }>;
  light1Label: string;
  light2Label: string;
  light3Label: string;
  light1Color: string;
  light2Color: string;
  light3Color: string;
  worker1Label: string;
  worker1Color: string;

  constructor(private workstationService: WorkstationService) {
  }

  ngOnInit(): void {
    this.poller = interval(500)
    .pipe(
      switchMap(() => this.workstationService.get('sub', 1)),
      tap(lights => {
        Object.keys(lights).forEach(key => {
          this[key + 'Color'] = lights[key]['color'] === 'off' ? '' : lights[key]['color'];
          this[key + 'Label'] = lights[key]['label'];
        });
      })
    );
  }

}
