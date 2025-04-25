import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LeaveserviceService {

  constructor() { }
}

import { Injectable } from '@angular/core'; import { HttpClient } from '@angular/common/http'; @Injectable({ providedIn: 'root' }) export class LeaveService { constructor(private http: HttpClient) {} applyForLeave(leave: any) { return this.http.post('/api/lms/leave/apply', leave); } }