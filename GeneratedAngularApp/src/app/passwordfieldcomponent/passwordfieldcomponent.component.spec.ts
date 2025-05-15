import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PasswordfieldcomponentComponent } from './passwordfieldcomponent.component';

describe('PasswordfieldcomponentComponent', () => {
  let component: PasswordfieldcomponentComponent;
  let fixture: ComponentFixture<PasswordfieldcomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PasswordfieldcomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PasswordfieldcomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
