import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QrcodecomponentComponent } from './qrcodecomponent.component';

describe('QrcodecomponentComponent', () => {
  let component: QrcodecomponentComponent;
  let fixture: ComponentFixture<QrcodecomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [QrcodecomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(QrcodecomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
