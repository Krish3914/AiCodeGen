import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PodserviceService {

  constructor() { }
}

import { Injectable } from '@angular/core'; import { HttpClient } from '@angular/common/http'; @Injectable({ providedIn: 'root' }) export class PodService { constructor(private http: HttpClient) {} getPodDetails(podId: any) { return this.http.get('/api/pods/details', { params: { podId: podId } }); } }