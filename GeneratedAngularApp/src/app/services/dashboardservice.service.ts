import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DashboardserviceService {

  constructor() { }
}

import { Injectable } from '@angular/core'; import { HttpClient } from '@angular/common/http'; @Injectable({ providedIn: 'root' }) export class DashboardService { constructor(private http: HttpClient) {} getDashboardData() { return this.http.get('/api/dashboard'); } }