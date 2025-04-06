import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LeavemanagementserviceService {

  constructor() { }
}

import { Injectable } from '@angular/core'; import { HttpClient } from '@angular/common/http'; @Injectable({ providedIn: 'root' }) export class LeaveManagementService { constructor(private http: HttpClient) {} applyForLeave(leave: any) { return this.http.post('/api/lms/leave/apply', leave); } approveLeave(leaveId: string, status: string) { return this.http.post('/api/lms/leave/approve', { leaveId, status }); } }