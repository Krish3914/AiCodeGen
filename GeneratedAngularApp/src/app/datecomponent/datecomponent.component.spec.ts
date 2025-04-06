import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DatecomponentComponent } from './datecomponent.component';

describe('DatecomponentComponent', () => {
  let component: DatecomponentComponent;
  let fixture: ComponentFixture<DatecomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DatecomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DatecomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
