import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Company } from '../interfaces/company';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class CompanyService {
  BASE_URL = 'http://localhost:8000/api';

  constructor(private client: HttpClient) {}

  getCompanies(): Observable<Company[]> {
    return this.client.get<Company[]>(`${this.BASE_URL}/companies/`);
  }

  getCompanyVacancies(id: number) {
    return this.client.get(`${this.BASE_URL}/companies/${id}/vacancies/`);
  }
}