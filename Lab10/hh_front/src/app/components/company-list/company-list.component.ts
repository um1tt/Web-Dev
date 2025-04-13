import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common'; 
import { CompanyService } from '../../services/company.service'; 
import { Company } from '../../interfaces/company'; 
import { Vacancy } from '../../interfaces/vacancy'; 

@Component({
  selector: 'app-company-list',
  standalone: true,
  imports: [ CommonModule ], 
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css'] 
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];
  vacancies: Vacancy[] = [];
  companyWasSelected: boolean = false; 

  constructor(private companyService: CompanyService) { }

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe({
      next: (data: Company[]) => { 
        this.companies = data || [];
        console.log("Компании загружены:", this.companies);
      },
      error: (err) => {
        console.error('Ошибка загрузки компаний:', err);
        this.companies = []; 
      }
    });
  }

  showVacancies(companyId: number): void {
    console.log("Запрос вакансий для компании с ID:", companyId);
    this.companyWasSelected = true; 
    this.vacancies = []; 
    this.companyService.getCompanyVacancies(companyId).subscribe({
      next: (data: any) => { 
          console.log('Получены сырые данные вакансий:', data);
          let vacanciesArray: Vacancy[] = [];
    
          if (Array.isArray(data)) {
              vacanciesArray = data;
          } else {
              
              console.warn('Ожидался массив вакансий, получен другой тип:', data);
          }
          this.vacancies = vacanciesArray;
          console.log("Вакансии установлены:", this.vacancies);
      },
      error: (err) => {
        console.error(`Ошибка загрузки вакансий для компании ${companyId}:`, err);
        this.vacancies = []; 
      }
    });
  }
}