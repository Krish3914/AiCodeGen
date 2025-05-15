import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LabelcomponentComponent } from './labelcomponent.component';

describe('LabelcomponentComponent', () => {
  let component: LabelcomponentComponent;
  let fixture: ComponentFixture<LabelcomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LabelcomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LabelcomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
