import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LeavemanagementsystemcomponentComponent } from './leavemanagementsystemcomponent.component';

describe('LeavemanagementsystemcomponentComponent', () => {
  let component: LeavemanagementsystemcomponentComponent;
  let fixture: ComponentFixture<LeavemanagementsystemcomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LeavemanagementsystemcomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LeavemanagementsystemcomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
