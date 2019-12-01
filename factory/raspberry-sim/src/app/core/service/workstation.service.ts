import {Injectable} from '@angular/core';
import {ApiService} from './api.service';
import {Observable, of} from 'rxjs';
import {ILight} from '../models';

@Injectable({
  providedIn: 'root'
})
export class WorkstationService {

  constructor(private api: ApiService) {
  }

  get(path: string, workstationNumber?: number): Observable<{ [key: string]: ILight }> {
    try {
      return this.api.get(`${path}${workstationNumber === undefined ? '' : workstationNumber}`);
    } catch(e) {
      console.log('Failed to execute GET request. Is the service down?');
    }
    // if (workstationNumber === 1) {
    //   return of({
    //     'light1': {'label': '', 'color': 'yellow'},
    //     'light2': {'label': '', 'color': 'yellow'},
    //     'light3': {'label': '', 'color': 'off'},
    //     'worker1': {'label': '', 'color': 'red'}
    //   });
    // } else if (workstationNumber === 2) {
    //   return of({
    //     'light1': {'label': '', 'color': 'yellow'},
    //     'light2': {'label': '', 'color': 'yellow'},
    //     'worker2': {'label': '', 'color': 'red'}
    //   });
    // } else if (path === 'main') {
    //   return of({
    //     'light1': {'label': '', 'color': 'off'},
    //     'light2': {'label': '', 'color': 'off'},
    //     'light3': {'label': '', 'color': 'off'},
    //     'light4': {'label': '', 'color': 'off'},
    //     'light5': {'label': '', 'color': 'off'},
    //     'light6': {'label': '', 'color': 'off'},
    //     'worker3': {'label': '', 'color': 'off'}
    //   });
    // }
  }

}
