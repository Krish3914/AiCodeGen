import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthserviceService {

  constructor() { }
}

import { Injectable } from '@angular/core'; import { HttpClient } from '@angular/common/http'; @Injectable({ providedIn: 'root' }) export class AuthService { constructor(private http: HttpClient) {} login(user: any) { return this.http.post('/api/auth/login', user); } getCurrentUser() { return this.http.get('/api/auth/me'); } }