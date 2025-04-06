import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NamecomponentComponent } from './namecomponent.component';

describe('NamecomponentComponent', () => {
  let component: NamecomponentComponent;
  let fixture: ComponentFixture<NamecomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NamecomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(NamecomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
