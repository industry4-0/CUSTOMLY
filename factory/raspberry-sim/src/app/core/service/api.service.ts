import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import {environment} from '../../../environments/environment';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {}

  private formatErrors(error: any) {
    return throwError(error.error);
  }

  get(path: string, params: HttpParams = new HttpParams(), responseType?): Observable<any> {
    return this.http.get(`${environment.apiUrl}${path}`, { params, responseType }).pipe(catchError(this.formatErrors));
  }

  put(path: string, body: object = {}, params: HttpParams = new HttpParams()): Observable<any> {
    return this.http
      .put(`${environment.apiUrl}${path}`, JSON.stringify(body), {
        headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
        params
      })
      .pipe(catchError(this.formatErrors));
  }

  post(path: string, body: object = {}, params: HttpParams = new HttpParams(), responseType?): Observable<any> {
    return this.http
      .post(`${environment.apiUrl}${path}`, JSON.stringify(body), {
        headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
        params,
        responseType
      })
      .pipe(catchError(this.formatErrors));
  }

  delete(path: string): Observable<any> {
    return this.http.delete(`${environment.apiUrl}${path}`).pipe(catchError(this.formatErrors));
  }
}
