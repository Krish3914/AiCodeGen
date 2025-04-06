import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TextfieldcomponentComponent } from './textfieldcomponent.component';

describe('TextfieldcomponentComponent', () => {
  let component: TextfieldcomponentComponent;
  let fixture: ComponentFixture<TextfieldcomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TextfieldcomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TextfieldcomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
