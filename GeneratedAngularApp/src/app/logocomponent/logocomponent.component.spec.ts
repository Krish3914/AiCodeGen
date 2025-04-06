import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LogocomponentComponent } from './logocomponent.component';

describe('LogocomponentComponent', () => {
  let component: LogocomponentComponent;
  let fixture: ComponentFixture<LogocomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LogocomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LogocomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
